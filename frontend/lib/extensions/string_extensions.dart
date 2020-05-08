import 'package:edgevalue/datamodels/routing_data.dart';

extension StringExtensions on String {
  RoutingData get getRoutingData {
    var uriData = Uri.parse(this);
    print('queryParameters: ${uriData.queryParameters} path: ${uriData.path}'); // TODO: remove this
    return RoutingData(
      queryParameters: uriData.queryParameters,
      route: uriData.path,
    );
  }
}
