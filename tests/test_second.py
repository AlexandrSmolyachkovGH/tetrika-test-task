from unittest.mock import patch, Mock

from tasks.task2.solution import parse_animals_from_html, fetch_html


def test_fetch_html_success():
    fake_html = "<html><body>Пример</body></html>"

    mock_response = Mock()
    mock_response.text = fake_html
    mock_response.encoding = 'utf-8'

    with patch("tasks.task2.solution.requests.get", return_value=mock_response) as mock_get:
        result = fetch_html("https://fake.url")
        assert result == fake_html
        mock_get.assert_called_once_with("https://fake.url", timeout=10)


def test_parse_animals_from():
    result = {}
    html = '''
    <div id="mw-pages">
        <div class="mw-content-ltr">
            <li><a href="/wiki/Аист">Аист</a></li>
            <li><a href="/wiki/Бобр">Бобр</a></li>
            <li><a href="/wiki/Баран">Баран</a></li>
            <li><a href="/wiki/Woolf">Woolf</a></li>
        </div>
    </div>
    '''
    parse_animals_from_html(html, result)
    assert result == {
        'А': 1,
        'Б': 2,
    }
