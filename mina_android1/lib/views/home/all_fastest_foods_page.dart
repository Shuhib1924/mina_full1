import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:mina_fixed1/common/app_style.dart';
import 'package:mina_fixed1/common/back_ground_container.dart';
import 'package:mina_fixed1/common/reusable_text.dart';
import 'package:mina_fixed1/common/shimmers/foodlist_shimmer.dart';
import 'package:mina_fixed1/constants/constants.dart';
import 'package:mina_fixed1/hooks/fetch_all_foods.dart';
import 'package:mina_fixed1/models/foods_model.dart';
import 'package:mina_fixed1/views/home/widgets/food_tile.dart';

class AllFastestFoods extends HookWidget {
  const AllFastestFoods({super.key});

  @override
  Widget build(BuildContext context) {
    final hookResult = useFetchAllFoods("41007428");
    List<FoodsModel>? foods = hookResult.data;
    final isLoading = hookResult.isLoading;
    return Scaffold(
      backgroundColor: kSecondary,
      appBar: AppBar(
        elevation: 0,
        backgroundColor: kSecondary,
        title: ReusableText(
            text: "Fastest Foods",
            style: appStyle(13, kLightWhite, FontWeight.w600)),
      ),
      body: BackGroundContainer(
        color: Colors.white,
        child: isLoading
            ? const FoodsListShimmer()
            : Padding(
                padding: EdgeInsets.all(12.h),
                child: ListView(
                  children: List.generate(foods!.length, (i) {
                    FoodsModel food = foods[i];
                    return FoodTile(
                      food: food,
                    );
                  }),
                ),
              ),
      ),
    );
  }
}
