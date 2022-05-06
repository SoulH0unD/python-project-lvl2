TEST_PLAIN_JSON = ("").join(["{'follow': {'type': 'REMOVED', 'value': 'false'}, ",
                "'host': {'type': 'EQUALS', 'value': 'hexlet.io'}, 'proxy': {'type': ",
                "'REMOVED', 'value': '123.234.53.22'}, 'timeout': {'type': 'CHANGED', ",
                "'old_value': 50, 'new_value': 20}, 'verbose': {'type': 'ADDED', 'value': 'true'}}"])
TEST_PLAIN_YAML = ("").join(["{'follow': {'type': 'REMOVED', 'value': 'false'}, ",
                "'host': {'type': 'EQUALS', 'value': 'hexlet.io'}, 'proxy': {'type': ",
                "'REMOVED', 'value': '123.234.53.22'}, 'timeout': {'type': 'CHANGED', ", 
                "'old_value': '50', 'new_value': '20'}, 'verbose': {'type': 'ADDED', 'value': 'true'}}"])
TEST_STAYLISH_JSON = ("").join(["{'common': {'type': 'NESTED', 'value': {'follow': {'type': 'ADDED', 'value': 'false'}, ",
                "'setting1': {'type': 'EQUALS', 'value': 'Value 1'}, 'setting2': {'type': 'REMOVED', 'value': 200}, 'setting3': ",
                "{'type': 'CHANGED', 'old_value': 'true', 'new_value': 'null'}, 'setting4': {'type': 'ADDED', 'value': 'blah blah'}, ",
                "'setting5': {'type': 'ADDED', 'value': {'key5': 'value5'}}, 'setting6': {'type': 'NESTED', 'value': {'doge': {'type': ",
                "'NESTED', 'value': {'wow': {'type': 'CHANGED', 'old_value': '', 'new_value': 'so much'}}}, 'key': {'type': 'EQUALS', ",
                "'value': 'value'}, 'ops': {'type': 'ADDED', 'value': 'vops'}}}}}, 'group1': {'type': 'NESTED', 'value': {'baz': {'type': ",
                "'CHANGED', 'old_value': 'bas', 'new_value': 'bars'}, 'foo': {'type': 'EQUALS', 'value': 'bar'}, 'nest': {'type': 'CHANGED', ",
                "'old_value': {'key': 'value'}, 'new_value': 'str'}}}, 'group2': {'type': 'REMOVED', 'value': {'abc': 12345, 'deep': {'id': 45}}}, ",
                "'group3': {'type': 'ADDED', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}"])
TEST_STAYLISH_YAML = ("").join(["{'common': {'type': 'NESTED', 'value': {'follow': {'type': 'ADDED', 'value': 'false'}, ",
                "'setting1': {'type': 'EQUALS', 'value': 'Value 1'}, 'setting2': {'type': 'REMOVED', 'value': '200'}, 'setting3': ",
                "{'type': 'CHANGED', 'old_value': 'true', 'new_value': 'null'}, 'setting4': {'type': 'ADDED', 'value': 'blah blah'}, ",
                "'setting5': {'type': 'ADDED', 'value': {'key5': 'value5'}}, 'setting6': {'type': 'NESTED', 'value': {'doge': {'type': ",
                "'NESTED', 'value': {'wow': {'type': 'CHANGED', 'old_value': '', 'new_value': 'so much'}}}, 'key': {'type': 'EQUALS', ",
                "'value': 'value'}, 'ops': {'type': 'ADDED', 'value': 'vops'}}}}}, 'group1': {'type': 'NESTED', 'value': {'baz': {'type': ",
                "'CHANGED', 'old_value': 'bas', 'new_value': 'bars'}, 'foo': {'type': 'EQUALS', 'value': 'bar'}, 'nest': {'type': 'CHANGED', ",
                "'old_value': {'key': 'value'}, 'new_value': 'str'}}}, 'group2': {'type': 'REMOVED', 'value': {'abc': '12345', 'deep': {'id': '45'}}}, ",
                "'group3': {'type': 'ADDED', 'value': {'deep': {'id': {'number': '45'}}, 'fee': '100500'}}}"])
TEST_STAYLISH_RENDER = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
TEST_PLAIN_RENDER = """Property 'common.follow' was added with value: 'false'
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From 'true' to 'null'
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: '[complex value]'
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From '[complex value]' to 'str'
Property 'group2' was removed
Property 'group3' was added with value: '[complex value]'"""
TEST_JSON_RENDER = ('').join(['{"common": {"type": "NESTED", "value": {"follow": {"type": "ADDED", "value": "false"}, ',
                '"setting1": {"type": "EQUALS", "value": "Value 1"}, "setting2": {"type": "REMOVED", "value": 200}, "setting3": ',
                '{"type": "CHANGED", "old_value": "true", "new_value": "null"}, "setting4": {"type": "ADDED", "value": "blah blah"}, ',
                '"setting5": {"type": "ADDED", "value": {"key5": "value5"}}, "setting6": {"type": "NESTED", "value": {"doge": {"type": ',
                '"NESTED", "value": {"wow": {"type": "CHANGED", "old_value": "", "new_value": "so much"}}}, "key": {"type": "EQUALS", ',
                '"value": "value"}, "ops": {"type": "ADDED", "value": "vops"}}}}}, "group1": {"type": "NESTED", "value": {"baz": {"type": ',
                '"CHANGED", "old_value": "bas", "new_value": "bars"}, "foo": {"type": "EQUALS", "value": "bar"}, "nest": {"type": "CHANGED", ',
                '"old_value": {"key": "value"}, "new_value": "str"}}}, "group2": {"type": "REMOVED", "value": {"abc": 12345, "deep": {"id": 45}}}, ',
                '"group3": {"type": "ADDED", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}}}'])