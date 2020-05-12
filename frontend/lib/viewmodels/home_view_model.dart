import 'package:flutter/material.dart';
import 'package:edgevalue/routing/route_names.dart';
import 'package:edgevalue/locator.dart';
import 'package:edgevalue/services/navigation_service.dart';

class HomeViewModel extends ChangeNotifier {
  final TextEditingController _controller = TextEditingController();
  TextEditingController get controller => _controller;

  void navigateToCompanyView() {
    locator<NavigationService>().navigateTo('$CompaniesRoute/${_controller.text}');
  }
}
