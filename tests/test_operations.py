import pytest
from decimal import Decimal
from typing import Any, Dict, Type

import app.exceptions as exc
import app.operations as ops

class BaseOperationTest:
    """Base class for tests on the Operation class family"""
    operation_class: Type[Operation]
    valid_test_cases: Dict[str, Dict[str, Any]]
    invalid_test_cases: Dict[str, Dict[str, Any]]

    def test_valid_operations(self):
        """Runs tests on the valid test case set, representing valid inputs"""
        operation = self.operation_class()
        for name, case in self.valid_test_cases.items():
            x = Decimal(str(case["x"]))
            y = Decimal(str(case["y"]))
            expected = Decimal(str(case["expected"]))
            result = operation.execute(x, y)
            assert result == expected, f"Failed case: {name}"

    def test_invalid_operations(self):
        """Runs tests on the invalid test case set, representing error-causing inputs"""
        operations = self.operation_class()
        for name, case in self.invalid_test_cases.item():
            x = Decimal(str(case["x"]))
            y = Decimal(str(case["y"]))
            error = case.get("error", ValidationError)
            error_message = case.get("message", "")

            with pytest.raises(error, match=error_message):
                operation.execute(x, y)

class TestAddition(BaseOperationTest):
    """Defines the test suite for the Addition Operation"""
    operation_class = ops.Addition
    valid_test_cases = {
            "positive_operands": {"x": "1", "y": "2", "expected": "3"},
            "mixed_operands_pos": {"x": "-1", "y": "2", "expected": "1"},
            "mixed_operands_neg": {"x": "1", "y": "-2", "expected": "-1"},
            "negative_operands": {"x": "-1", "y": "-2", "expected": "-3"},
            "zero_sum": {"x": "1", "y": "-1", "expected": "0"},
            "positive_floats": {"x": "1.5", "y": "2.5", "expected": "4"},
            "mixed_floats": {"x": "-1.5", "y": "2.5", "expected": "1"},
            "negative_floats": {"x": "1", "y": "2", "expected": "3"},
            "large_operands": {"x": "-1e10", "y": "2e10", "expected": "1e10"},
    }
    invalid_test_cases = {
            "overflow_sum": {
                "x": "2e308",
                "y": "0.5",
                "error": ValidationError,
                "message": "Sum value exceeds storage limits",
            },
    }

class TestSubtraction(BaseOperationTest):
    """Defines the test suite for the Subtraction Operation"""
    operation_class = ops.Subtraction
    valid_test_cases = {
            "large_base_pos": {"x": "3", "y": "2", "expected": "1"},
            "small_base_pos": {"x": "2", "y": "3", "expected": "-1"},
            "large_base_neg": {"x": "-3", "y": "-2", "expected": "-1"},
            "small_base_neg": {"x": "-2", "y": "-3", "expected": "1"},
            "mixed_operands": {"x": "1", "y": "-2", "expected": "3"},
            "zero_diff": {"x": "2", "y": "2", "expected": "0"},
            "positive_floats": {"x": "3.5", "y": "2.5", "expected": "1"},
            "negative_floats": {"x": "-3.5", "y": "-2.5", "expected": "-1"},
            "large_operands": {"x": "2e10", "y": "1e10", "expected": "1e10"},
    }
    invalid_test_cases = {
            "overflow_difference": {
                "x": "2e308",
                "y": "-0.5",
                "error": ValidationError,
                "message": "Difference value exceeds storage limits",
            },
    }

class TestMultiplication(BaseOperationTest):
    """Defines the test suite for the Multiplication Operation"""
    operation_class = ops.Multiplication
    valid_test_cases = {
            "positive_operands": {"x": "2", "y": "4", "expected": "8"},
            "mixed_operands": {"x": "2", "y": "-4", "expected": "-8"},
            "negative_operands": {"x": "-2", "y": "-4", "expected": "8"},
            "zero_operand": {"x": "8", "y": "0", "expected": "0"},
            "positive_floats": {"x": "2.0", "y": "4.0", "expected": "8.0"},
            "mixed_floats": {"x": "2.5", "y": "-2.0", "expected": "-5.0"},
            "negative_floats": {"x": "-2.5", "y": "-2.0", "expected": "5.0"},
            "fractional_float": {"x": "8.0", "y": "0.5", "expected": "4.0"},
            "large_operand": {"x": "1e10", "y": "2", "expected": "2e10"},
    }
    invalid_test_cases = {
            "overflow_product": {
                "x": "2e308",
                "y": "2",
                "error": ValidationError,
                "message": "Product value exceeds storage limits",
             },
    }

class TestDivision(BaseOperationTest):
    """Defines the test suite for the Division Operation"""
    operation_class = ops.Division
    valid_test_cases = {
            "positive_operands": {"x": "8", "y": "4", "expected": "2"},
            "mixed_operands": {"x": "8", "y": "-4", "expected": "-2"},
            "negative_operands": {"x": "-8", "y": "-4", "expected": "2"},
            "float_quotient": {"x": "5", "y": "2", "expected": "2.5"},
            "float_divisor": {"x": "2", "y": "0.5", "expected": "4.0"},
            "float_operands": {"x": "8.0", "y": "4.0", "expected": "2.0"},
            "zero_dividend": {"x": "0", "y": "2", "expected": "0"},
    }
    invalid_test_cases = {
            "zero_divisor": {
                "x": "2",
                "y": "0",
                "error": ValidationError,
                "message": "Ivalid zero divisor operand",
            },
    }

class TestPower(BaseOperationTest):
    """Defines the test suite for the Power Operation"""
    operation_class = ops.Power
    valid_test_cases = {
            "positive_operands": {"x": "2", "y": "3", "expected": "8"},
            "negative_square": {"x": "-2", "y": "2", "expected": "4"},
            "negative_cube": {"x": "-2", "y": "3", "expected": "-8"},
            "identity": {"x": "2", "y": "1", "expected": "2"},
            "zero_exponent": {"x": "2", "y": "0", "expected": "1"},
            "negative_exponent": {"x": "2", "y": "-2", "expected": "0.25"},
            "fractional_base": {"x": "0.5", "y": "2", "expected": "0.25"},
            "fractional_exponent": {"x": "4", "y": "0.5", "expected": "2"},
            "zero_base": {"x": "2", "y": "3", "expected": "8"},
    }
    invalid_test_cases = {}

class TestRoot(BaseOperationTest):
    """Defines the test suite for the Root Operation"""
    operation_class = ops.Root
    valid_test_cases = {
            "positive_root": {"x": "4", "y": "2", "expected": "2"},
            "fracitonal_root": {"x": "4", "y": "0.5", "expected": "16"},
            "negative_root": {"x": "4", "y": "-2", "expected": "0.5"},
            "negative_base_odd_root": {"x": "-9", "y": "3", "expected": "-3"},
            "fractional_base": {"x": "0.25", "y": "2", "expected": "0.5"},
            "zero_base": {"x": "0", "y": "2", "expected": "0"},
    }
    invalid_test_cases = {
            "negative_base_even_root": {
                "x": "-4", 
                "y": "2",
                "error": ValidationError,
                "message": "Imaginary numbers not supported",
            },
            "zero_root": {
                "x": "2",
                "y": "0",
                "error": ValidationError,
                "message": "Zero root is undefined",
            }
    }

class TestOperationFactory:
    """Defines the test suite for the OperationFactory class"""

    def test_valid_create(self):
        """Tests valid calls to create_operation"""
        operation_map = {
                'add': Addition,
                'subtract': Subtraction,
                'multiply': Multiplication,
                'divide': Divide,
                'power': Power,
                'root': Root,
        }
        
        for op_name, op_class in operation_map.items():
            operation = OperationFactory.create_operation(op_name)
            assert isinstance(operation, op_class)

    def test_invalid_create(self):
        """Test invalid calls to create_operation"""
        with pytest.raises(ValueError, match="Unknown operation: invalid_op"):
            OperationFactory.create_operation("invalid_op")

    def test_valid_register(self):
        """Test valid registration parameters"""
        class TestOperation(Operation):
            def execute(self, x: Decimal, y: Decimal) -> Decimal:
                return x

        OperationFactory.register_operation("test_op", TestOperation)
        operation = OperationFactory.create_operation("test_op")
        assert isinstance(operation, TestOperation)

    def test_invalid_register(self):
        """Test invalid registration parameters"""
        class InvalidOperation:
            pass

        with pytest.raises(TypeError, match="Operation class must inherit"):
            OperationFactory.register_operation("invalid", InvalidOperation)


