import 'package:flutter/material.dart';
import 'package:edgevalue/routing/route_names.dart';
import 'package:edgevalue/views/home_view/home_view.dart';
import 'package:edgevalue/views/company_view/company_view.dart';
import 'package:edgevalue/datamodels/routing_data.dart';
import 'package:edgevalue/extensions/string_extensions.dart';

Route<dynamic> generateRoute(RouteSettings routeSettings) {
  RoutingData routingData = routeSettings.name.getRoutingData;

  switch (routingData.route) {
    case HomeRoute:
      return _getPageRoute(routeSettings, HomeView());
    case CompanyRoute:
      int companyId = int.tryParse(routingData['id']);
      return _getPageRoute(routeSettings, CompanyView(companyId: companyId,));
    default:
      return null;
  }
}

/*
 * We are creating a new `PageRoute`, so we have to
 * pass it the current `RouteSettings`.
 */
PageRoute _getPageRoute(RouteSettings settings, Widget child) {
  return _NoAnimationPageRoute(
    child: child,
    settings: settings
  );
}

class _NoAnimationPageRoute extends PageRouteBuilder {
  final Widget child;
  final RouteSettings settings;

  _NoAnimationPageRoute({this.child, this.settings}) : super(
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
    settings: settings,
  );
}
