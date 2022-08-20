
import tempfile

import prewl

class TestConfig:
    def test_dict(self):
        prewl.reset_config()
        assert 'test' not in prewl.CONFIG
        prewl.configure({'test': 123})
        assert 'test' in prewl.CONFIG
        assert prewl.CONFIG['test'] == 123
    
    def test_file(self):
        prewl.reset_config()
        with tempfile.NamedTemporaryFile() as tmp:
            with open(tmp.name, 'w') as f:
                f.write('{"test": 123}')
            assert 'test' not in prewl.CONFIG
            prewl.configure(tmp.name)
            assert 'test' in prewl.CONFIG
            assert prewl.CONFIG['test'] == 123