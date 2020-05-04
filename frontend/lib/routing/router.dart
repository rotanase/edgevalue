import 'package:flutter/material.dart';
import 'package:edgevalue/routing/route_names.dart';
import 'package:edgevalue/views/home_view/home_view.dart';
import 'package:edgevalue/views/company_view/company_view.dart';

Route<dynamic> generateRoute(RouteSettings settings) {
  switch (settings.name) {
    case HomeRoute:
      return _getPageRoute(HomeView());
    case CompanyRoute:
      return _getPageRoute(CompanyView());
    default:
      return null; // TODO: Add a custom not found page
  }
}

PageRoute _getPageRoute(Widget child) {
  return _NoAnimationPageRoute(child: child);
}

class _NoAnimationPageRoute extends PageRouteBuilder {
  final Widget child;

  _NoAnimationPageRoute({this.child}) : super(
    pageBuilder: (
      BuildContext context,
      Animation<double> animation,
      Animation<double> secondaryAnimation,
    ) => child,
    transitionsBuilder: (
      BuildContext context,
      Animation<double> animation,
      Animation<double> secondaryAnimation,
      Widget child,
    ) => FadeTransition(
      opacity: animation,
      child: child,
    ),
  );
}
