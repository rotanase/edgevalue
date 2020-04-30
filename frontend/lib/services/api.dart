import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:edgevalue/datamodels/company_item_model.dart';

class Api {
  static const String _apiEndpoint =  'http://192.168.99.100/api/v1';

  Future<dynamic> getCompanies() async {
    var response = await http.get('$_apiEndpoint/companies');
    if (response.statusCode == 200) {
      var companies = (json.decode(response.body) as List)
        .map((company) => CompanyItemModel.fromJson(company))
        .toList();
      return companies;
    }

    return null;
  }
}
