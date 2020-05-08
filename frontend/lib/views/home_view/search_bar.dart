import 'package:flutter/material.dart';
import 'package:responsive_builder/responsive_builder.dart';
import 'package:edgevalue/viewmodels/search_bar_view_model.dart';

import 'search_bar_desktop.dart';

class SearchBar extends StatelessWidget {
  final SearchBarViewModel viewModel;

  SearchBar({@required this.viewModel});

  @override
  Widget build(BuildContext context) {
    return ScreenTypeLayout(
      // TODO: mobile navigation bar
      desktop: SearchBarDesktop(viewModel: viewModel),
    );
  }
}
