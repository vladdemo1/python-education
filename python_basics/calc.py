"""This module contains the main class - Calculator with an initial set of functions"""


class Calc:
    """This Calculator class represents 4 simple steps: Add, Sub, Multiply, Divide"""
    @staticmethod
    def add(numerator, denominator):
        """The operation of adding two numbers"""
        return numerator + denominator

    @staticmethod
    def subtract(numerator, denominator):
        """The operation of subtracting two numbers"""
        return numerator - denominator

    @staticmethod
    def multiply(numerator, denominator):
        """The operation of multiplying two numbers"""
        return numerator * denominator

    @staticmethod
    def divide(numerator, denominator):
        """The operation of dividing two numbers"""
        if denominator == 0:
            return "U can't use 0 in second value for divide"
        return numerator / denominator
