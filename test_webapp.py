import webapp
import json
import mock

def test_httpify_should_prepend_http_to_adress_without_http():
    assert webapp.httpify('vg.no') == 'http://vg.no'

def test_httpify_should_not_prepend_when_adress_already_has_http():
    assert webapp.httpify('http://vg.no') == 'http://vg.no'

def test_httpify_should_strip_whitescpace():
    assert webapp.httpify(' http://vg.no ') == 'http://vg.no'

def test_get_hello_world_is_a_json_response_that_returns_200_ok():
    response = webapp.app.test_client().get('/hello-world')
    assert response.content_type == 'application/json'
    assert json.loads(response.data) == {'message': 'Hello, World!'}

@mock.patch('text.generate', return_value=['text'])
@mock.patch('html_parse.gather_headlines')
def test_get_urls_should_generate_200_ok_response(gather_headlines, generate):
    response = webapp.app.test_client().get('/vg.no,db.no')
    assert response.status_code == 200

@mock.patch('text.generate', return_value=['text'])
@mock.patch('html_parse.gather_headlines')
def test_get_urls_should_fetch_webpages(gather_headlines, generate):
    response = webapp.app.test_client().get('/vg.no,db.no')
    gather_headlines.assert_called_with(['http://vg.no', 'http://db.no'])

@mock.patch('text.generate', return_value=['text'])
@mock.patch('html_parse.gather_headlines')
def test_get_urls_should_generate_text_and_return_it_as_a_json_object(gather_headlines, generate):
    response = webapp.app.test_client().get('/vg.no,db.no')
    assert json.loads(response.data) == {'generated': ['text']}

@mock.patch('text.generate', return_value=['text'])
@mock.patch('html_parse.gather_headlines', return_value=['headline1', 'head line 2'])
@mock.patch('text.chain_from')
def test_get_urls_should_invoke_generate_correctly(chain_from, gather_headlines, generate):
    response = webapp.app.test_client().get('/vg.no,db.no')
    chain_from.assert_called_with([['headline1'], ['head', 'line', '2']])
