class CalculatorModel {
  static const operations = const ['%', '÷', '+', '-', 'x'];

  String result = '0';

  CalculatorModel() {
    _clear();
  }

  void _clear() {
    result = '';
  }

  void applyCommand(String command) {
    if (command == '=') {
      _calculate();
    } else if (command == 'AC') {
      _clear();
    } else if (command == 'DEL') {
      deleteEndDigit();
    } else {
      _addDigit(command);
    }
  }

  void deleteEndDigit() {
    result = result.length > 1 ? result.substring(0, result.length - 1) : '0';
  }

  void _addDigit(String digit) {
    if (result == '0') {
      result = digit;
    } else {
      result += digit;
    }
  }

  double _calculate() {
    final digitsString = result.split(RegExp(r"(?<=[-+x÷%])|(?=[-+x÷%])"));

    if (digitsString.length < 2) {
      return double.tryParse(digitsString.elementAt(0));
    }

    var newResult;
    var operation;

    for (var element in digitsString) {
      if (operations.contains(element)) {
        operation = element;
      } else if (newResult == null) {
        newResult = double.parse(digitsString.elementAt(0));
      } else if (operation != null) {
        final numberB = double.parse(element);
        newResult = resolveOperation(newResult, numberB, operation);
      }
    }

    result = newResult.toString();
    return newResult ?? '0';
  }

  double resolveOperation(numberA, numberB, operation) {
    switch (operation) {
      case '%':
        return numberA % numberB;
      case '÷':
        return numberA / numberB;
      case 'x':
        return numberA * numberB;
      case '+':
        return numberA + numberB;
      case '-':
        return numberA - numberB;
      default:
        return 0.0;
    }
  }
}
