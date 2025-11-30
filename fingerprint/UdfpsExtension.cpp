/*
 * Copyright (C) 2022 The LineageOS Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the Licese is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <stdint.h>
#include <compositionengine/UdfpsExtension.h>

uint32_t getUdfpsZOrder(uint32_t z, bool touched) {
    (void) touched;
    return z;
}

uint64_t getUdfpsUsageBits(uint64_t usageBits, bool touched) {
    if (touched) {
        usageBits |= 0x400000000LL;
    }
    return usageBits;
}

// This is the new function required for LineageOS 21 (Android 14)
uint32_t getUdfpsDimZOrder(uint32_t z) {
    // This ensures the dim layer is stacked correctly
    // on top of other surfaces.
    return z | 0x10000000;
}

