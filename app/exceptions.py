"""This module provides a family of exceptions for calculation-related errors"""

class CalculatorError(Exception):
    pass

#class ConfigurationError(CalculatorError):
#    pass

class OperationError(CalculatorError):
    pass

class ValidationError(CalculatorError):
    pass
