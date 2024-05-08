from abc import ABC, abstractmethod

# Step 1: Define the Component Interface
class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text: str) -> str:
        pass

# Step 2: Implement Concrete Components
class BaseTextProcessor(TextProcessor):
    def process_text(self, text: str) -> str:
        text = "Welcome Here" + " " + text
        return text

# Step 3: Create Decorator Classes
class UppercaseDecorator(TextProcessor):
    def __init__(self, component: TextProcessor):
        self.component = component
    
    def process_text(self, text: str) -> str:
        return self.component.process_text(text).upper()

class RemoveSpacesDecorator(TextProcessor):
    def __init__(self, component: TextProcessor):
        self.component = component
    
    def process_text(self, text: str) -> str:
        return self.component.process_text(text).replace(' ', '')

# Step 4: Use Decorators
base_processor = BaseTextProcessor()
print("Base Text Processor:", base_processor.process_text("Hello, World!"))

uppercase_processor = UppercaseDecorator(base_processor)
print("Uppercase Text Processor:", uppercase_processor.process_text("Hello, World!"))

remove_spaces_processor = RemoveSpacesDecorator(base_processor)
print("Remove Spaces Text Processor:", remove_spaces_processor.process_text("Hello, World!"))

uppercase_remove_spaces_processor = UppercaseDecorator(RemoveSpacesDecorator(base_processor))
print("Uppercase Remove Spaces Text Processor:", uppercase_remove_spaces_processor.process_text("Hello, World!"))
