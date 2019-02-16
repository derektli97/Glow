//
// DO NOT EDIT.
//
// Generated by the protocol buffer compiler.
// Source: grpc.proto
//

//
// Copyright 2018, gRPC Authors All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
import Foundation
import Dispatch
import SwiftGRPC
import SwiftProtobuf

internal protocol Glow_GlowTestPointReceivingCall: ClientCallUnary {}

fileprivate final class Glow_GlowTestPointReceivingCallBase: ClientCallUnaryBase<Glow_PointRequest, Glow_GlowReply>, Glow_GlowTestPointReceivingCall {
  override class var method: String { return "/glow.Glow/TestPointReceiving" }
}


/// Instantiate Glow_GlowServiceClient, then call methods of this protocol to make API calls.
internal protocol Glow_GlowService: ServiceClient {
  /// Synchronous. Unary.
  func testPointReceiving(_ request: Glow_PointRequest) throws -> Glow_GlowReply
  /// Asynchronous. Unary.
  func testPointReceiving(_ request: Glow_PointRequest, completion: @escaping (Glow_GlowReply?, CallResult) -> Void) throws -> Glow_GlowTestPointReceivingCall

}

internal final class Glow_GlowServiceClient: ServiceClientBase, Glow_GlowService {
  /// Synchronous. Unary.
  internal func testPointReceiving(_ request: Glow_PointRequest) throws -> Glow_GlowReply {
    return try Glow_GlowTestPointReceivingCallBase(channel)
      .run(request: request, metadata: metadata)
  }
  /// Asynchronous. Unary.
  internal func testPointReceiving(_ request: Glow_PointRequest, completion: @escaping (Glow_GlowReply?, CallResult) -> Void) throws -> Glow_GlowTestPointReceivingCall {
    return try Glow_GlowTestPointReceivingCallBase(channel)
      .start(request: request, metadata: metadata, completion: completion)
  }

}

