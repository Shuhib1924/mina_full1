import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:mina_fixed1/constants/constants.dart';
import 'package:mina_fixed1/models/api_eror.dart';
import 'package:mina_fixed1/models/hook_models/restaurant_hook.dart';
import 'package:mina_fixed1/models/restaurants_model.dart';
import 'package:http/http.dart' as http;

FetchRestaurant useFetchRestaurant(String code) {
  final restaurants = useState<RestaurantsModel?>(null);
  final isLoading = useState<bool>(false);
  final error = useState<Exception?>(null);
  final appiError = useState<ApiError?>(null);

  Future<void> fetchData() async {
    isLoading.value = true;

    try {
      Uri url = Uri.parse('$appBaseUrl/api/restaurant/byId/$code');
      final response = await http.get(url);

      if (response.statusCode == 200) {
        var restaurant = jsonDecode(response.body);
        restaurants.value = RestaurantsModel.fromJson(restaurant);
      } else {
        appiError.value = apiErrorFromJson(response.body);
      }
    } catch (e) {
      debugPrint(e.toString());
    } finally {
      isLoading.value = false;
    }
  }

  useEffect(() {
    fetchData();
    return null;
  }, []);

  void refetch() {
    isLoading.value = true;
    fetchData();
  }

  return FetchRestaurant(
    data: restaurants.value,
    isLoading: isLoading.value,
    error: error.value,
    refetch: refetch,
  );
}
