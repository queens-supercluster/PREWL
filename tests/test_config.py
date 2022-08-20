
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
    
    def test_hybrid(self):
        prewl.reset_config()
        assert 'test1' not in prewl.CONFIG
        assert 'test2' not in prewl.CONFIG
        assert 'test3' not in prewl.CONFIG
        prewl.configure({'test1': 123, 'test2': 123})
        assert prewl.CONFIG['test1'] == 123
        assert prewl.CONFIG['test2'] == 123

        with tempfile.NamedTemporaryFile() as tmp:
            with open(tmp.name, 'w') as f:
                f.write('{"test2": 321, "test3": 321}')
            prewl.configure(tmp.name)
            assert prewl.CONFIG['test1'] == 123
            assert prewl.CONFIG['test2'] == 321
            assert prewl.CONFIG['test3'] == 321
            