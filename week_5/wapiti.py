import os
from IPython.display import display, HTML
import glob
import pathlib


# Base 'out' name you passed to Wapiti (-o). Update if you used a different name.
out_name = "juice_wapiti_report.html"

def find_html_report(out):
# If out is a file and ends with .html, use it
    if os.path.isfile(out) and out.lower().endswith('.html'):
        return os.path.abspath(out)
    # If out is a directory, search for the newest .html inside it
    if os.path.isdir(out):
        matches = glob.glob(os.path.join(out, "*.html"))
        if matches:
        # choose the most recent file
            matches.sort(key=os.path.getmtime, reverse=True)
            return os.path.abspath(matches[0])
    # If out doesn't exist as provided, search for any html file pattern that looks like wapiti output
    candidates = glob.glob(out + "*/*.html") + glob.glob(out + "*.html")
    if candidates:
        candidates.sort(key=os.path.getmtime, reverse=True)
        return os.path.abspath(candidates[0])
    return None

report_path = find_html_report(out_name)
if report_path:
    print("Report file found:", report_path)
    try:
        with open(report_path, 'r', encoding='utf-8') as f:
            html = f.read()
        display(HTML(html))
    except Exception as e:
        print("Could not render HTML inline (error):", e)
        print("Open the file in your browser instead:", report_path)
else:
    print("No HTML report found. Check that the scan produced the report and that 'out_name' matches the -o argument passed to Wapiti.")


