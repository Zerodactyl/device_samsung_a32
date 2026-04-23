#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

#run PYTHONPATH=$PWD/tools/extract-utils python device/samsung/a32/extract-files.py

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/samsung/a32',
    'hardware/mediatek',
    'hardware/samsung',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib64/libnvram.so',
        'vendor/lib64/libsysenv.so',
        'vendor/bin/hw/android.hardware.neuralnetworks@1.3-service-mtk-neuron',
        'vendor/bin/hw/samsung.software.media.c2@1.0-service',
        'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b'): blob_fixup()
        .add_needed('libbase_shim.so'),

    (
        'vendor/bin/hw/vendor.samsung.hardware.light-service',
        'vendor/lib64/vendor.samsung.hardware.light-V1-ndk_platform.so'): blob_fixup()
        .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),

    (
        'vendor/lib/sensors.inputvirtual.so',
        'vendor/lib/sensors.sensorhub.so',
        'vendor/lib64/sensors.inputvirtual.so',
        'vendor/lib64/sensors.sensorhub.so',
        'vendor/lib/hw/audio.primary.mt6768.so',
        'vendor/bin/hw/vendor.samsung.hardware.camera.provider@4.0-service_64'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v31.so'),

     'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .add_needed('libgraphicbuffersource_shim.so')
        .add_needed('libui_shim.so'),

     'vendor/bin/hw/samsung.software.media.c2@1.0-service': blob_fixup()
        .add_needed('libui_shim.so')
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v31.so'),

     'vendor/bin/hw/vendor.samsung.hardware.camera.provider@4.0-service_64': blob_fixup()
        .add_needed('libprocessgroup_shim.so')
        .replace_needed('libbinder.so', 'libbinder-v31.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v31.so'),

     'vendor/bin/hw/vendor.samsung.hardware.hyper-service': blob_fixup()
        .replace_needed('liblog.so', 'liblog-v31.so'),

     'vendor/etc/init/android.hardware.media.c2@1.2-mediatek.rc': blob_fixup()
        .regex_replace('/vendor/bin/hw/android.hardware.media.c2@1.2-mediatek', '/vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b'),
}  # fmt: skip

module = ExtractUtilsModule(
    'a32',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
