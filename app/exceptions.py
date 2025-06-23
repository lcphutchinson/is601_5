"""This module provides a family of exceptions for calculation-related errors"""

class CalculatorError(Exception):
    """Base exception class for errors concerning Calculator components"""
    pass

#class ConfigurationError(CalculatorError):
#    pass

class SerializationError(CalculatorError):
    """
    Raised when data serialization or deserialization fails.

    This exception is triggered when the system is unable to transform data to and
    from dictionary encoding, or when errors arise reading data from or writing data to files.
    """
    pass

class ValidationError(CalculatorError):
    pass
