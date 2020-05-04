import 'package:flutter/material.dart';
import 'package:edgevalue/locator.dart';
import 'package:edgevalue/services/api.dart';
import 'package:edgevalue/datamodels/company_item_model.dart';

class SearchResultsViewModel {
  final Api _api = locator<Api>();

  ListView _searchResults;
  ListView get searchResults => _searchResults;

  Future getSearchResults(String patternToSearch, Function notifyCallback) async {
    List<CompanyItemModel> companies = await _api.getCompanies();
    /*
     * Build `_searchResults` by filtering companies list
     * using `patternToSearch` string. As of now, filtering
     * is done in frontend.
     */
    if (companies != null) {
      companies = companies.where(
        (company) => company.matches(patternToSearch)
      ).toList();
      _searchResults = ListView.builder(
        padding: EdgeInsets.zero,
        shrinkWrap: true,
        itemCount: companies.length,
        itemBuilder: (BuildContext context, int index) => companies[index],
      );
    } // TODO: else show `Couldn't fetch data from server` error
    notifyCallback();
  }
}
