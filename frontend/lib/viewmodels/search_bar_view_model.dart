import 'package:flutter/material.dart';
import 'package:edgevalue/locator.dart';
import 'package:edgevalue/services/api.dart';
import 'package:edgevalue/datamodels/company_item_model.dart';
import 'package:edgevalue/routing/route_names.dart';
import 'package:edgevalue/services/navigation_service.dart';
import 'package:flutter/services.dart';

class SearchBarViewModel {
  final Api _api = locator<Api>();

  // Used to hide `_resultsOverlay` when this search bar looses
  // focus and to show it when it gains focus.
  final FocusNode _searchBarfocusNode = FocusNode();
  final FocusNode _keyboadListenerfocusNode = FocusNode();
  FocusNode get searchBarfocusNode => _searchBarfocusNode;
  FocusNode get keyboadListenerfocusNode => _keyboadListenerfocusNode;

  // `ListView` containing search results, used in the UI.
  ListView _searchResultsListView;
  ListView get searchResultsListView => _searchResultsListView;

  // List of search results.
  List<CompanyItemModel> _searchResults;

  // Current selected companyItemModel in search results.
  CompanyItemModel _selectedCompanyItemModel;

  // This informs that this view model is waiting for a response from `_api`.
  bool _waitingForResults = true;
  bool get waitingForResults => _waitingForResults;

  // Mouse pointer is hovering inside Overlay area.
  bool mouseHoveringResultsOverlayEntry = false;

  Future getSearchResults(String patternToSearch, Function notifyCallback) async {
    
    // Setting some variables before starting a search.
    {
      _waitingForResults = true;
    }

    // Getting a list of all companies from the backend.
    List<CompanyItemModel> companies = await _api.getCompanies();

    // Build `_searchResults` by filtering companies list
    // using `patternToSearch` string. As of now, filtering
    // is done in frontend.
    if (companies != null) {
      _searchResults = companies.where(
        (company) => company.matches(patternToSearch)
      ).toList();

      for (CompanyItemModel item in _searchResults) {
        item.resetAllSelected = _resetSelectedItemInSearchResultsList;
      }

      _searchResultsListView = ListView.builder(
        padding: EdgeInsets.zero,
        shrinkWrap: true,
        itemCount: _searchResults.length,
        itemBuilder: (BuildContext context, int index) => _searchResults[index],
      );
    } // TODO: else show `Couldn't fetch data from server` error

    // Search operation is now finished.
    {
      _waitingForResults = false;
      notifyCallback();
    }
  }

  void _resetSelectedItemInSearchResultsList() {
    for (CompanyItemModel item in _searchResults) {
      if (item.isSelected) {
        item.setSelected(false);
      }
    }
  }

  void _updateSelectedItemInSearchResultsList({bool downDirection = true}) {
    for (int i = 0; i < _searchResults.length; ++i) {
      if (_searchResults[i].isSelected) {
        int direction = downDirection ? 1 : -1;
        _searchResults[i].setSelected(false);
        _searchResults[(i + direction) % _searchResults.length].setSelected(true);
        return;
      }
    }

    _searchResults[0].setSelected(true);
  }

  void onKey(String inputText, RawKeyEvent event) {
    if (event.runtimeType == RawKeyUpEvent) {
      if (event.logicalKey.keyId == 4295426088) {
        // TODO: Replace this
        // Hack: This forces the removal of the `_resultsOverlayEntry`, remove
        // it by calling a `notifyCallback()`, similar to `getSearchResults()`.
        mouseHoveringResultsOverlayEntry = false;

        _navigateToCompanyView(inputText);
      }
    } else if (event.runtimeType == RawKeyDownEvent) {
      if (event.logicalKey.keyId == 4295426129) {
        _updateSelectedItemInSearchResultsList();
      } else if (event.logicalKey.keyId == 4295426130) {
        _updateSelectedItemInSearchResultsList(downDirection: false);
      }
    }
    _searchBarfocusNode?.requestFocus();
  }

  void onFieldSubmitted(String inputText) {
    _selectedCompanyItemModel = _searchResults?.firstWhere(
      (companyItemModel) => companyItemModel.isSelected,
      orElse: () => null,
    );
    _keyboadListenerfocusNode.requestFocus();
  }

  void onResultsOverlayEntryTap() {
    _selectedCompanyItemModel = _searchResults?.firstWhere(
      (companyItemModel) => companyItemModel.isSelected,
      orElse: () => null,
    );

    if (_selectedCompanyItemModel != null) {
      // TODO: Replace this
      // Hack: This forces the removal of the `_resultsOverlayEntry`, remove
      // it by calling a `notifyCallback()`, similar to `getSearchResults()`.
      mouseHoveringResultsOverlayEntry = false;

      _navigateToCompanyView('');
    }

    _searchBarfocusNode?.requestFocus();
  }

  void _navigateToCompanyView(String inputText) {
    String query = '$CompaniesRoute/';

    if (_selectedCompanyItemModel != null) {
      query += _selectedCompanyItemModel.ticker.toLowerCase();
      _selectedCompanyItemModel = null;
    } else if (_searchResults?.isNotEmpty ?? false) {
      query += _searchResults[0].ticker.toLowerCase();
    } else {
      query += inputText;
    }

    locator<NavigationService>().navigateTo(query);
  }
}
