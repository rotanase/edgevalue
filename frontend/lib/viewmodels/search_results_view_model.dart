import 'package:flutter/material.dart';
import 'package:edgevalue/locator.dart';
import 'package:edgevalue/services/api.dart';
import 'package:edgevalue/datamodels/company_item_model.dart';

class SearchResultsViewModel {
  final Api _api = locator<Api>();

  ListView _searchResults;
  ListView get searchResults => _searchResults;

  // As of now, filter of the companies is done in frontend.
  Future getSearchResults(String pattern, Function notifyCallback) async {
    print ('Hello2');
    List<CompanyItemModel> companies = await _api.getCompanies();

    print ('Hello3');
    if (companies != null) {
      print ('Hello4');
      companies = companies.map((company) =>
        company.name.contains(pattern) ||
        company.ticker.contains(pattern) ||
        company.isin.contains(pattern) ? company : null,
      );
      
      _searchResults = ListView.builder(
        itemCount: companies.length,
        itemBuilder: (BuildContext context, int index) {
          return companies[index];
        },
      );
    }

    notifyCallback();
  }
}
