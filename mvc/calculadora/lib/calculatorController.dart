import 'calculatorModel.dart';

class CalculatorController {
  final calculatorModel = new CalculatorModel();

  String getResult() {
    return calculatorModel.result;
  }

  void applyCommand(String command) {
    calculatorModel.applyCommand(command);
  }
}
