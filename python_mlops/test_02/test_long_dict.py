def test_long_dictionaries():
    
    result = {'key': 'value', 'lastname': 'deza', 'firstname': 'alfredo'}
    expected = {'key': 'value', 'lastname': 'deza', 'firstname': 'alfredo'}
    
    assert result['key'] == expected['key']
    assert result['firstname'] == expected['firstname']
    assert result == expected