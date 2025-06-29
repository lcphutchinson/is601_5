"""This module provides an input sanitation service for the calculator repl"""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Any

from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError

@dataclass
class InputValidator:
    """Container class for validation & sanitation methods"""

    @staticmethod
    def validate_number(value: Any, config: CalculatorConfig) -> Decimal:
        """
        Validate a numerical input to Decimal

        Parameters
        ----------
        value: Any
            An input value to validate
        config: CalculatorConfig
            The configuration settings for this session

        Raises
        ------
        ValidationError:
            if an invalid input is provided

        Returns
        -------
        Decimal:
            A Decimal representation of the input
        """
        if isinstance(value, str):
            value = value.strip()
        try:
            num = Decimal(str(value))
            if abs(num) > config.max_input_value:
                raise ValidationError(
                    f"Value exceeds allowed maximum: {config.max_input_value}")
            return num.normalize()
        except InvalidOperation:
            raise ValidationError(f"Invalid number format: {value}")
