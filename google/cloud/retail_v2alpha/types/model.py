# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2alpha.types import common

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "Model",
    },
)


class Model(proto.Message):
    r"""Metadata that describes the training and serving parameters of a
    [Model][google.cloud.retail.v2alpha.Model]. A
    [Model][google.cloud.retail.v2alpha.Model] can be associated with a
    [ServingConfig][google.cloud.retail.v2alpha.ServingConfig] and then
    queried through the Predict api.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        page_optimization_config (google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig):
            Optional. The page optimization config.

            This field is a member of `oneof`_ ``training_config``.
        name (str):
            Required. The fully qualified resource name of the model.

            Format:
            projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}
            catalog_id has char limit of 50. recommendation_model_id has
            char limit of 40.
        display_name (str):
            Required. The display name of the model.
            Should be human readable, used to display
            Recommendation Models in the Retail Cloud Cosole
            Dashboard. UTF-8 encoded string with limit of
            1024 characters.
        training_state (google.cloud.retail_v2alpha.types.Model.TrainingState):
            Optional. The training state that the model
            is in (e.g. TRAINING or PAUSED).

            Since part of the cost of running the service is
            frequency of training - this can be used to
            determine when to train model in order to
            control cost. If not specified: the default
            value for CreateModel method is TRAINING. the
            default value for UpdateModel method is to keep
            the state the same as before.
        serving_state (google.cloud.retail_v2alpha.types.Model.ServingState):
            Output only. The serving state of the model: ACTIVE,
            NOT_ACTIVE.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the Recommendation
            Model was created at.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the Recommendation
            Model was last updated. E.g. if a Recommendation
            Model was paused - this would be the time the
            pause was initiated.
        type_ (str):
            Required. The type of model e.g. ``home-page``.

            Currently supported values: ``recommended-for-you``,
            ``others-you-may-like``, ``frequently-bought-together``,
            ``page-optimization``, 'similar-items', 'buy-it-again',
            ``recently-viewed``\ (readonly value).
        optimization_objective (str):
            Optional. The optimization objective e.g. ``cvr``.

            Currently supported values: ``ctr``, ``cvr``,
            ``revenue-per-order``.

            If not specified, we choose default based on model type.
            Default depends on type of recommendation:

            ``recommended-for-you`` => ``ctr``

            ``others-you-may-like`` => ``ctr``

            ``frequently-bought-together`` => ``revenue_per_order``
        periodic_tuning_state (google.cloud.retail_v2alpha.types.Model.PeriodicTuningState):
            Optional. The state of periodic tuning.

            The period we use is 3 months - to do a one-off tune earlier
            use the TuneModel method. Default value is
            PERIODIC_TUNING_ENABLED.
        last_tune_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the latest
            successful tune finished.
        tuning_operation (str):
            Output only. The tune operation associated
            with the model.
            Can be used to determine if there is an ongoing
            tune for this recommendation. Empty field
            implies no tune is goig on.
        data_state (google.cloud.retail_v2alpha.types.Model.DataState):
            Output only. The state of data requirements for this model:
            DATA_OK and DATA_ERROR.

            Recommendation model cannot be trained if the data is in
            DATA_ERROR state. Recommendation model can have DATA_ERROR
            state even if serving state is ACTIVE: models were trained
            successfully before, but cannot be refreshed because model
            no longer has sufficient data for training.
        filtering_option (google.cloud.retail_v2alpha.types.RecommendationsFilteringOption):
            Optional. If RECOMMENDATIONS_FILTERING_ENABLED,
            recommendation filtering by attributes is enabled for the
            model.
        serving_config_lists (Sequence[google.cloud.retail_v2alpha.types.Model.ServingConfigList]):
            Output only. The list of valid serving
            configs associated with the
            PageOptimizationConfig.
    """

    class ServingState(proto.Enum):
        r"""The serving state of the model."""
        SERVING_STATE_UNSPECIFIED = 0
        INACTIVE = 1
        ACTIVE = 2
        TUNED = 3

    class TrainingState(proto.Enum):
        r"""The training state of the model."""
        TRAINING_STATE_UNSPECIFIED = 0
        PAUSED = 1
        TRAINING = 2

    class PeriodicTuningState(proto.Enum):
        r"""Describes whether periodic tuning is enabled for this model
        or not. Periodic tuning is scheduled at most every three months.
        You can start a tuning process manually by using the ModelTune
        method, which starts a tuning process immediately and resets the
        quarterly schedule. Enabling or disabling periodic tuning does
        not affect any current tuning processes.
        """
        PERIODIC_TUNING_STATE_UNSPECIFIED = 0
        PERIODIC_TUNING_DISABLED = 1
        ALL_TUNING_DISABLED = 3
        PERIODIC_TUNING_ENABLED = 2

    class DataState(proto.Enum):
        r"""Describes whether this model have sufficient training data
        to be continuously trained.
        """
        DATA_STATE_UNSPECIFIED = 0
        DATA_OK = 1
        DATA_ERROR = 2

    class PageOptimizationConfig(proto.Message):
        r"""The PageOptimizationConfig for model training.

        This determines how many panels to optimize for, and which serving
        configurations to consider for each panel. The purpose of this model
        is to optimize which
        [ServingConfig][google.cloud.retail.v2alpha.ServingConfig] to show
        on which panels in way that optimizes the visitors shopping journey.

        Attributes:
            page_optimization_event_type (str):
                Required. The type of
                [UserEvent][google.cloud.retail.v2alpha.UserEvent] this page
                optimization is shown for.

                Each page has an associated event type - this will be the
                corresponding event type for the page that the page
                optimization model is used on.

                Supported types:

                -  ``add-to-cart``: Products being added to cart.
                -  ``detail-page-view``: Products detail page viewed.
                -  ``home-page-view``: Homepage viewed
                -  ``category-page-view``: Homepage viewed
                -  ``shopping-cart-page-view``: User viewing a shopping
                   cart.

                ``home-page-view`` only allows models with type
                ``recommended-for-you``. All other
                page_optimization_event_type allow all
                [Model.types][google.cloud.retail.v2alpha.Model.type].
            panels (Sequence[google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig.Panel]):
                Required. A list of panel configurations.
                Limit = 5.
            restriction (google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig.Restriction):
                Optional. How to restrict results across panels e.g. can the
                same
                [ServingConfig][google.cloud.retail.v2alpha.ServingConfig]
                be shown on multiple panels at once.

                If unspecified, default to ``UNIQUE_MODEL_RESTRICTION``.
        """

        class Restriction(proto.Enum):
            r"""Restrictions of expected returned results."""
            RESTRICTION_UNSPECIFIED = 0
            NO_RESTRICTION = 1
            UNIQUE_SERVING_CONFIG_RESTRICTION = 2
            UNIQUE_MODEL_RESTRICTION = 3
            UNIQUE_MODEL_TYPE_RESTRICTION = 4

        class Candidate(proto.Message):
            r"""A candidate to consider for a given panel. Currently only
            [ServingConfig][google.cloud.retail.v2alpha.ServingConfig] are valid
            candidates.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                serving_config_id (str):
                    This has to be a valid
                    [ServingConfig][google.cloud.retail.v2alpha.ServingConfig]
                    identifier. e.g. for a ServingConfig with full name:
                    ``projects/*/locations/global/catalogs/default_catalog/servingConfigs/my_candidate_config``
                    this would be 'my_candidate_config'

                    This field is a member of `oneof`_ ``candidate``.
            """

            serving_config_id = proto.Field(
                proto.STRING,
                number=1,
                oneof="candidate",
            )

        class Panel(proto.Message):
            r"""An individual panel with a list of
            [ServingConfigs][google.cloud.retail.v2alpha.ServingConfig] to
            consider for it.

            Attributes:
                display_name (str):
                    Optional. The name to display for the panel.
                candidates (Sequence[google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig.Candidate]):
                    Required. The candidates to consider on the
                    panel.
                    Limit = 10.
                default_candidate (google.cloud.retail_v2alpha.types.Model.PageOptimizationConfig.Candidate):
                    Required. The default candidate (in case the
                    model fails at serving time, we can fall back to
                    the default).
            """

            display_name = proto.Field(
                proto.STRING,
                number=1,
            )
            candidates = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="Model.PageOptimizationConfig.Candidate",
            )
            default_candidate = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Model.PageOptimizationConfig.Candidate",
            )

        page_optimization_event_type = proto.Field(
            proto.STRING,
            number=1,
        )
        panels = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Model.PageOptimizationConfig.Panel",
        )
        restriction = proto.Field(
            proto.ENUM,
            number=3,
            enum="Model.PageOptimizationConfig.Restriction",
        )

    class ServingConfigList(proto.Message):
        r"""Represents an ordered combination of valid serving configs, which /
        may be used for PAGE_OPTIMIZATION recommendations.

        Attributes:
            serving_config_ids (Sequence[str]):
                Optional. A set of valid serving configs that may be used
                for PAGE_OPTIMIZATION.
        """

        serving_config_ids = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    page_optimization_config = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="training_config",
        message=PageOptimizationConfig,
    )
    name = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name = proto.Field(
        proto.STRING,
        number=2,
    )
    training_state = proto.Field(
        proto.ENUM,
        number=3,
        enum=TrainingState,
    )
    serving_state = proto.Field(
        proto.ENUM,
        number=4,
        enum=ServingState,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    type_ = proto.Field(
        proto.STRING,
        number=7,
    )
    optimization_objective = proto.Field(
        proto.STRING,
        number=8,
    )
    periodic_tuning_state = proto.Field(
        proto.ENUM,
        number=11,
        enum=PeriodicTuningState,
    )
    last_tune_time = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    tuning_operation = proto.Field(
        proto.STRING,
        number=15,
    )
    data_state = proto.Field(
        proto.ENUM,
        number=16,
        enum=DataState,
    )
    filtering_option = proto.Field(
        proto.ENUM,
        number=18,
        enum=common.RecommendationsFilteringOption,
    )
    serving_config_lists = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=ServingConfigList,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
