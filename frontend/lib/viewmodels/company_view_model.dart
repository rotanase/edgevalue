import 'package:flutter/material.dart';
import 'package:edgevalue/locator.dart';
import 'package:edgevalue/services/api.dart';
import 'package:edgevalue/datamodels/company_item_model.dart';

class CompanyViewModel extends ChangeNotifier {
  final _api = locator<Api>();

  String _companyName;
  String get companyName => _companyName;

  Future getCompanyData(int companyIndex) async {
    CompanyItemModel companyItemModel = await _api.getCompanyData(companyIndex);

    _companyName = companyItemModel?.name;
    notifyListeners();
  }
}
