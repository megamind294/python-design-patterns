from builder.report import ReportBuilder


if __name__ == "__main__":
    report = (
        ReportBuilder()
        .title("Security Review")
        .add_section("Findings", "Three issues found.")
        .include_summary("Prioritize authentication fixes.")
        .build()
    )
    print(report)
