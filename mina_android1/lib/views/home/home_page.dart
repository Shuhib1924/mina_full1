import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:mina_fixed1/common/custom_appbar.dart';
import 'package:mina_fixed1/common/custom_container.dart';
import 'package:mina_fixed1/common/heading.dart';
import 'package:mina_fixed1/constants/constants.dart';
import 'package:mina_fixed1/controllers/category_controller.dart';
import 'package:mina_fixed1/views/home/all_fastest_foods_page.dart';
import 'package:mina_fixed1/views/home/all_nearby_restaurants.dart';
import 'package:mina_fixed1/views/home/recommendations_page.dart';
import 'package:mina_fixed1/views/home/widgets/category_foods_list.dart';
import 'package:mina_fixed1/views/home/widgets/category_list.dart';
import 'package:mina_fixed1/views/home/widgets/food_list.dart';
import 'package:mina_fixed1/views/home/widgets/nearby_restaurants_list.dart';
import 'package:get/get.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = Get.put(CategoryController());
    return Scaffold(
      backgroundColor: kPrimary,
      appBar: PreferredSize(
          preferredSize: Size.fromHeight(130.h), child: const CustomAppBar()),
      body: SafeArea(
        child: CustomContainer(
            containerContent: Column(
          children: [
            const CategoryList(),
            Obx(
              () => controller.categoryValue == ''
                  ? Column(
                      children: [
                        Heading(
                          text: "Try Something New",
                          onTap: () {
                            Get.to(() => const RecommendationsPage(),
                                transition: Transition.cupertino,
                                duration: const Duration(milliseconds: 900));
                          },
                        ),
                        const FoodsList(),
                        Heading(
                          text: "Nearby Restaurants",
                          onTap: () {
                            Get.to(() => const AllNearbyRestaurants(),
                                transition: Transition.cupertino,
                                duration: const Duration(milliseconds: 900));
                          },
                        ),
                        const NearbyRestaurants(),
                        Heading(
                          text: "Food closer to you",
                          onTap: () {
                            Get.to(() => const AllFastestFoods(),
                                transition: Transition.cupertino,
                                duration: const Duration(milliseconds: 900));
                          },
                        ),
                        const FoodsList(),
                      ],
                    )
                  : CustomContainer(
                      containerContent: Column(
                      children: [
                        Heading(
                          more: true,
                          text: "Explore ${controller.titleValue} Category",
                          onTap: () {
                            Get.to(() => const RecommendationsPage(),
                                transition: Transition.cupertino,
                                duration: const Duration(milliseconds: 900));
                          },
                        ),
                        const CategoryFoodsList()
                      ],
                    )),
            )
          ],
        )),
      ),
    );
  }
}
