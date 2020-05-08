import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/search_bar/search_bar_desktop.dart' as widgets;
import 'package:edgevalue/localization/app_translations.dart';
import 'package:edgevalue/viewmodels/search_bar_view_model.dart';

class SearchBarDesktop extends StatelessWidget {

  // Used for the text field widget of this search bar.
  final SearchBarViewModel viewModel;

  SearchBarDesktop({@required this.viewModel});

  @override
  Widget build(BuildContext context) {
    return widgets.SearchBarDesktop(
      height: 50,
      width: 600,
      resultsOverlayWidth: 600,
      hintText: Translations.of(context).text('home_search_bar_initial_text'),
      viewModel: viewModel,
    );
  }
}
