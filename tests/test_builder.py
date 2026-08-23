from builder.report import ReportBuilder


def test_builder_constructs_report_with_chained_steps():
    report = (
        ReportBuilder()
        .title('Security Review')
        .add_section('Findings', 'Three issues found.')
        .include_summary('Prioritize authentication fixes.')
        .build()
    )

    assert report.title == 'Security Review'
    assert report.sections == (('Findings', 'Three issues found.'),)
    assert report.summary == 'Prioritize authentication fixes.'
