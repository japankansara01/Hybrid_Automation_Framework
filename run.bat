call D:\japan_office\feb\framework\.venv\Scripts\activate

rem chrome
pytest -s -v -m "sanity" --browser chrome
rem pytest -s -v -m "regression" --browser chrome
rem pytest -s -v -m "sanity and regression" --browser chrome

rem firefox
rem pytest -s -v -m "sanity" --browser firefox
rem pytest -s -v -m "regression" --browser firefox
rem pytest -s -v -m "sanity and regression" --browser firefox