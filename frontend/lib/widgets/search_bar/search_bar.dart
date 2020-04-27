import 'package:flutter/material.dart';
import 'package:responsive_builder/responsive_builder.dart';
import 'package:edgevalue/widgets/search_bar/search_bar_desktop.dart';

class SearchBar extends StatefulWidget {
  @override
  _SearchBarState createState() => _SearchBarState();
}

class _SearchBarState extends State<SearchBar> {
  @override
  Widget build(BuildContext context) {
    return ScreenTypeLayout(
      // TODO: mobile implementation
      desktop: SearchBarDesktop(),
    );
  }
}
