import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:edgevalue/locator.dart';
import 'package:edgevalue/localization/app_translations.dart';
import 'package:edgevalue/services/navigation_service.dart';
import 'package:edgevalue/routing/router.dart';
import 'package:edgevalue/routing/route_names.dart';

void main() {
  setupLocator();
  runApp(EdgeValue());
}

class EdgeValue extends StatefulWidget {
  @override
  _EdgeValueState createState() => _EdgeValueState();
}

class _EdgeValueState extends State<EdgeValue> {
  @override
  Widget build(BuildContext context) => MaterialApp(
    title: 'Edge Value',
    localizationsDelegates: [
      const TranslationsDelegate(),
      GlobalMaterialLocalizations.delegate,
      GlobalWidgetsLocalizations.delegate,
    ],
    supportedLocales: [
      const Locale('en', ''),
      const Locale('ro', ''),
    ],
    navigatorKey: locator<NavigationService>().navigatorKey,
    onGenerateRoute: generateRoute,
    initialRoute: HomeRoute,
  );
}
