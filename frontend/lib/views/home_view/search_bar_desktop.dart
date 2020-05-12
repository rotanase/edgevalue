import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/search_bar/search_bar_desktop.dart' as widgets;
import 'package:edgevalue/localization/app_translations.dart';

class SearchBarDesktop extends StatelessWidget {

  // Used for the text field widget of this search bar.
  final TextEditingController controller;

  SearchBarDesktop({@required this.controller});

  @override
  Widget build(BuildContext context) {
    return widgets.SearchBarDesktop(
      height: 50,
      width: 600,
      resultsOverlayWidth: 600,
      hintText: Translations.of(context).text('home_search_bar_initial_text'),
      controller: controller,
    );
  }
}
