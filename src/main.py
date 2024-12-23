from typing import Optional

class DataProcessor:
    def __init__(self, config: Optional[dict] = None):
        self.config = config or {}
    
    def process(self, data: str) -> str:
        return f'Processed: {data}'

def main():
    processor = DataProcessor()
    result = processor.process('test data')
    print(result)

if __name__ == '__main__':
    main()