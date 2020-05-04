import 'package:get_it/get_it.dart';
import 'package:edgevalue/services/navigation_service.dart';
import 'package:edgevalue/services/api.dart';

final GetIt locator = GetIt.instance;

void setupLocator() {
  locator.registerLazySingleton(() => NavigationService());
  locator.registerLazySingleton(() => Api());
}