from llama_parse import LlamaParse

class LlamaParser:
    def __init__(self, parsing_instruction):
        self.parser = LlamaParse(result_type="markdown", parsing_instruction=parsing_instruction)

    def parse_document(self, file_path):
        return self.parser.load_data(file_path)

    def save_to_markdown(self, documents, output_path):
        with open(output_path, 'w', encoding='utf-8') as f:
            for doc in documents:
                f.write(doc.text + '\n')
