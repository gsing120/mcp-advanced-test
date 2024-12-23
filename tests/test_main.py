from src.main import DataProcessor

def test_data_processor():
    processor = DataProcessor()
    result = processor.process('test')
    assert result == 'Processed: test'

def test_data_processor_with_config():
    processor = DataProcessor({'key': 'value'})
    assert processor.config == {'key': 'value'}