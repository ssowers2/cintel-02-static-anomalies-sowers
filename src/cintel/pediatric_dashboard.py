"""Create an interactive pediatric data quality dashboard."""

from pathlib import Path

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import polars as pl

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "pediatric_quality_data.csv"
ISSUES_FILE = PROJECT_ROOT / "artifacts" / "pediatric_quality_issues.csv"
OUTPUT_FILE = PROJECT_ROOT / "docs" / "assets" / "pediatric_dashboard.html"

COLORS = {
    "navy": "#183153",
    "teal": "#17A398",
    "coral": "#EF7868",
    "light": "#F5F8FC",
    "white": "#FFFFFF",
}


def main() -> None:
    """Read validation results and generate the dashboard."""
    records = pl.read_csv(DATA_FILE)
    issues = pl.read_csv(ISSUES_FILE)

    total = records.height
    flagged = issues.height
    passed = total - flagged
    pass_rate = passed / total if total else 0

    counts = issues.group_by("quality_issue").len().sort("len", descending=True)

    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[[{"type": "domain"}, {"type": "xy"}]],
        column_widths=[0.43, 0.57],
        horizontal_spacing=0.23,
        subplot_titles=("Validation Overview", "Issues by Category"),
    )

    # Donut chart
    fig.add_trace(
        go.Pie(
            labels=["Passed Checks", "Flagged for Review"],
            values=[passed, flagged],
            hole=0.75,
            marker={
                "colors": [COLORS["teal"], COLORS["coral"]],
                "line": {"color": "#333333", "width": 1},
            },
            textinfo="none",
            hovertemplate="%{label}: %{value} records<extra></extra>",
            showlegend=True,
            sort=False,
        ),
        row=1,
        col=1,
    )

    # Issue category chart
    fig.add_trace(
        go.Bar(
            x=counts["len"].to_list(),
            y=counts["quality_issue"].to_list(),
            orientation="h",
            marker={
                "color": COLORS["coral"],
                "line": {"color": "#333333", "width": 1},
            },
            text=counts["len"].to_list(),
            textposition="outside",
            cliponaxis=False,
            hovertemplate="%{y}: %{x} records<extra></extra>",
            showlegend=False,
        ),
        row=1,
        col=2,
    )

    # KPI cards
    kpis = [
        ("RECORDS ANALYZED", total, 0.02, COLORS["navy"]),
        ("PASSED CHECKS", passed, 0.35, COLORS["teal"]),
        ("FLAGGED FOR REVIEW", flagged, 0.68, COLORS["coral"]),
    ]

    for label, value, x, color in kpis:
        fig.add_shape(
            type="rect",
            xref="paper",
            yref="paper",
            x0=x,
            x1=x + 0.30,
            y0=1.12,
            y1=1.35,
            fillcolor=COLORS["white"],
            line={"color": "#444444", "width": 1},
            layer="below",
        )

        # Controls the words RECORDS ANALYZED, PASSED CHECKS, and FLAGGED FOR REVIEW
        fig.add_annotation(
            x=x + 0.15,
            y=1.29,
            xref="paper",
            yref="paper",
            xanchor="center",
            yanchor="middle",
            text=label,
            showarrow=False,
            font={"size": 11, "color": COLORS["navy"]},
            align="center",
        )

        # Controls the numbers 50, 37, and 13.
        # Center the KPI numbers inside each card
        fig.add_annotation(
            x=x + 0.15,
            y=1.22,
            xref="paper",
            yref="paper",
            xanchor="center",
            yanchor="middle",
            text=f"<b>{value}</b>",
            showarrow=False,
            font={"size": 29, "color": color},
            align="center",
        )

        # Center label inside the donut
        # Center the percentage using the donut chart's actual position
        donut_domain = fig.data[0].domain

        fig.add_annotation(
            text=f"<b>{pass_rate:.0%}</b><br>Passed",
            x=(donut_domain.x[0] + donut_domain.x[1]) / 2,
            y=(donut_domain.y[0] + donut_domain.y[1]) / 2,
            xref="paper",
            yref="paper",
            xanchor="center",
            yanchor="middle",
            showarrow=False,
            font={"size": 25, "color": COLORS["navy"]},
            align="center",
        )

        fig.update_layout(
            title={
                "text": (
                    "<b>Pediatric Data Quality Dashboard</b>"
                    "<br><sup>Fictional Patient Records | "
                    "Completeness & Validity Checks</sup>"
                ),
                "x": 0.5,
                "y": 0.96,
            },
            font={"family": "Arial", "color": COLORS["navy"]},
            paper_bgcolor=COLORS["light"],
            plot_bgcolor=COLORS["light"],
            height=720,
            margin={"l": 60, "r": 65, "t": 250, "b": 95},
            showlegend=True,
            legend={
                "orientation": "h",
                "x": 0.5,
                "xanchor": "center",
                "y": -0.18,
            },
            bargap=0.30,
        )

    fig.update_xaxes(
        showgrid=False,
        title_text="Number of Records",
        rangemode="tozero",
    )

    fig.update_yaxes(
        showgrid=False,
        autorange="reversed",
        ticklabelstandoff=12,
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(OUTPUT_FILE, include_plotlyjs="cdn", full_html=True)

    print(f"Dashboard created successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
