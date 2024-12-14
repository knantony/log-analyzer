class ReportGenerator:
    @staticmethod
    def generate_report(analysis_result, output_path):
        with open(output_path, 'w') as file:
            file.write("Log Analysis Report\n")
            file.write("===================\n\n")
            file.write(f"1. Total Log Entries: {analysis_result['total_logs']}\n")
            file.write(f"2. Error Rate: {analysis_result['error_rate']:.2f}%\n\n")

            if analysis_result['most_frequent_error']:
                most_error, count = analysis_result['most_frequent_error'][0]
                file.write(f"3. Most Frequent Log Entry:\n- ERROR: {most_error} ({count} occurrences)\n\n")

            if analysis_result['warnings']:
                file.write("4. Warnings:\n")
                for warning, count in analysis_result['warnings']:
                    file.write(f"- WARN: {warning} ({count} occurrences)\n")
