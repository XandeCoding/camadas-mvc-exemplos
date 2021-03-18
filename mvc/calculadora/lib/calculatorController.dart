import 'calculatorModel.dart';

class CalculatorController {
  final calculatorModel = new CalculatorModel();

  String getResult() {
    return calculatorModel.result;
  }

  void addToCalc(String command) {
    calculatorModel.applyCommand(command);
  }
}
