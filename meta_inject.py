from pathlib import Path

META_TAG = '<meta name="google-site-verification" content="bdRA19J2H65oQLkOCEzn_mZZ-sSyXAf9LERxVsMFftA" />'
SITE_DIR = 'site'

def inject_meta(file_path: Path):
    content = file_path.read_text("utf-8")
    if META_TAG not in content:
      # Insert after <head> tag
      new_content = content.replace('<head>', f'<head>\n    {META_TAG}', 1)
      file_path.write_text(new_content, "utf-8")

for html_file in Path(SITE_DIR).rglob('*.html'):
    inject_meta(html_file)
