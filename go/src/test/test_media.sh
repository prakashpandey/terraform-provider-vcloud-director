#*****************************************************************
# terraform-provider-vcloud-director
# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause
#*****************************************************************

export TF_ACC=1
export TF_LOG=INFO


. ./test_setlogin.sh

export TF_VAR_MEDIA_PATH="/home/Core-9.0.iso"

go test github.com/vmware/terraform-provider-vcloud-director/go/src/vcd/provider/ -v -run TestAccResourceCatalogItemMedia | grep --line-buffered -vE 'TRACE|terraform|^$'
status=${PIPESTATUS[0]} 


#go test -v 2>&1 | go-junit-report > report.xml
echo "test_media.sh EXIT STATUS = " $status

exit $status

