import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:mina_fixed1/constants/constants.dart';
import 'package:mina_fixed1/models/api_eror.dart';
import 'package:mina_fixed1/models/hook_models/hook_result.dart';
import 'package:mina_fixed1/models/restaurants_model.dart';
import 'package:http/http.dart' as http;

FetchHook useFetchAllRestaurants(String code) {
  final restaurants = useState<List<RestaurantsModel>?>(null);
  final isLoading = useState<bool>(false);
  final error = useState<Exception?>(null);
  final appiError = useState<ApiError?>(null);

  Future<void> fetchData() async {
    isLoading.value = true;

    try {
      Uri url = Uri.parse('$appBaseUrl/api/restaurant/all/$code');
      final response = await http.get(url);
      if (response.statusCode == 200) {
        restaurants.value = restaurantsModelFromJson(response.body);
      } else {
        appiError.value = apiErrorFromJson(response.body);
      }
    } catch (e) {
      error.value = e as Exception;
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

  return FetchHook(
    data: restaurants.value,
    isLoading: isLoading.value,
    error: error.value,
    refetch: refetch,
  );
}
