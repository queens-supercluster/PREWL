
import tempfile

import prewl

class TestConfig:
    def test_dict(self):
        assert 'gpu' not in prewl.CONFIG
        prewl.configure({'gpu': True})
        assert 'gpu' in prewl.CONFIG
        assert prewl.CONFIG['gpu']
    
    def test_file(self):
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.write("{'gpu': true}")
            assert 'gpu' not in prewl.CONFIG
            prewl.configure(tmp.name)
            assert 'gpu' in prewl.CONFIG
            assert prewl.CONFIG['gpu']