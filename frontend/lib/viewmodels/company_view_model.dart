import 'package:flutter/material.dart';
import 'package:edgevalue/locator.dart';
import 'package:edgevalue/services/api.dart';
import 'package:edgevalue/datamodels/company_item_model.dart';
import 'package:edgevalue/extensions/string_extensions.dart';
import 'package:edgevalue/datamodels/routing_data.dart';
import 'package:edgevalue/routing/route_names.dart';

import 'dart:developer' as developer;

class CompanyViewModel extends ChangeNotifier {
  final _api = locator<Api>();

  String _companyName;
  String get companyName => _companyName;
  
  Future _getCompanyData(String companyTicker) async {
    CompanyItemModel companyItemModel = await _api.getCompanyData(companyTicker);
    if (companyItemModel != null) {
      _companyName = companyItemModel.name;
    } else {
      // TODO: Send to error page with message 'Company not found'
      _companyName = 'No company with id $companyTicker';
    }

    notifyListeners();
  }

  /*
   * At this point the Uri shoul look like: `/companies/[ticker][?id=id]`,
   * where `ticker` or `id` is optional.
   */
  Future getCompanyByUri(String uri) async {
    RoutingData routingData = uri.getRoutingData;
    try {
      // We get the ticker by ignoring `/companies/`.
      String companyTicker = routingData.route.substring(CompaniesRoute.length + 1);
      if (companyTicker.isNotEmpty) {
        return await _getCompanyData(companyTicker);
      }
    } catch (exception) {
      developer.log("No ticker in Uri: $uri");
    }
    
    // TODO: else send to error page with message 'Invalid Request'  
  }
}
