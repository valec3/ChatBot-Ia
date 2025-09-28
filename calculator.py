class Calculator:
    def get_operation_from_prompt(self, prompt):
        # Extraer la operación matemática del prompt
        for char in prompt:
            if char not in "0123456789+-*/(). ":
                prompt = prompt.replace(char, " ")
        return prompt.strip()
    def calculate(self, prompt):
        operation = self.get_operation_from_prompt(prompt)
        try:
            result = eval(operation)
            return result, True
        except Exception as e:
            return f"Error al calcular: {e}", False
        return None