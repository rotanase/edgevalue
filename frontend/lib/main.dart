import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:edgevalue/views/layout_template.dart';
import 'package:edgevalue/localization/app_translations.dart';

void main() => runApp(EdgeValue());

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
    home: LayoutTemplate(),
  );
}
